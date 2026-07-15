"""
SINTA MCP Server — cek skor dan profil peneliti Indonesia.
Scraping dari sinta.kemdiktisaintek.go.id
"""
import json, re
import httpx
from bs4 import BeautifulSoup
from fastmcp import FastMCP

mcp = FastMCP("sinta")
BASE = "https://sinta.kemdiktisaintek.go.id"

@mcp.tool()
async def sinta_search_dosen(query: str) -> str:
    """Cari profil dosen di SINTA berdasarkan nama atau NIDN"""
    try:
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as c:
            r = await c.get(f"{BASE}/authors", params={"q": query})
            soup = BeautifulSoup(r.text, "html.parser")
            results = []
            for item in soup.select(".author-item")[:10]:
                name_el = item.select_one("h4 a")
                affil = item.select_one(".affil")
                score = item.select_one(".score")
                if name_el:
                    results.append({
                        "nama": name_el.text.strip(),
                        "link": f"{BASE}{name_el.get('href','')}",
                        "afiliasi": affil.text.strip() if affil else "-",
                        "skor": score.text.strip() if score else "-"
                    })
            if not results:
                # Fallback: coba ambil dari teks biasa
                texts = [t.strip() for t in soup.text.split('\n') if query.lower() in t.lower()][:5]
                return json.dumps({"pencarian": query, "hasil": texts or ["Tidak ditemukan"]}, indent=2, ensure_ascii=False)
            return json.dumps({"pencarian": query, "hasil": results}, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2, ensure_ascii=False)

@mcp.tool()
async def sinta_detail_dosen(url: str) -> str:
    """Lihat detail profil dosen dari URL SINTA (contoh: /authors/123456)"""
    try:
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as c:
            full_url = f"{BASE}{url}" if url.startswith("/") else url
            r = await c.get(full_url)
            soup = BeautifulSoup(r.text, "html.parser")
            data = {"url": full_url}
            
            # Nama
            name = soup.select_one(".profile-name")
            if name: data["nama"] = name.text.strip()
            
            # Skor
            scores = soup.select(".score-box")
            for s in scores:
                label = s.select_one(".label")
                value = s.select_one(".value")
                if label and value:
                    data[label.text.strip()] = value.text.strip()
            
            # Publikasi terbaru
            pubs = []
            for pub in soup.select(".pub-item")[:5]:
                title = pub.select_one("h5 a")
                year = pub.select_one(".year")
                if title:
                    pubs.append({
                        "judul": title.text.strip(),
                        "tahun": year.text.strip() if year else "-"
                    })
            if pubs:
                data["publikasi"] = pubs
                
            return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2, ensure_ascii=False)

@mcp.tool()
async def sinta_search_jurnal(query: str = "", akreditasi: str = "") -> str:
    """Cari jurnal terindeks SINTA berdasarkan nama atau tingkat akreditasi (S1-S6)"""
    try:
        params = {}
        if query: params["q"] = query
        if akreditasi: params["accreditation"] = akreditasi
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as c:
            r = await c.get(f"{BASE}/journals", params=params)
            soup = BeautifulSoup(r.text, "html.parser")
            results = []
            # Coba berbagai selector (SINTA pake JS, mungkin perlu fallback)
            for item in soup.select(".journal-item, .card-journal, tr")[:15]:
                texts = [t.strip() for t in item.stripped_strings if t.strip()]
                if texts and any(len(t) > 20 for t in texts):
                    results.append({"konten": texts[:5]})
            if not results:
                # Fallback: ambil teks yang mengandung kata kunci
                texts = [t.strip() for t in soup.text.split('\n') if t.strip() and len(t.strip()) > 30][:10]
                hasil = [{"judul": t} for t in texts] if texts else [{"pesan": "Halaman menggunakan JavaScript. Coba buka langsung: https://sinta.kemdiktisaintek.go.id/journals"}]
                return json.dumps({"pencarian": query, "akreditasi": akreditasi, "hasil": hasil}, indent=2, ensure_ascii=False)
            return json.dumps({"pencarian": query, "akreditasi": akreditasi, "hasil": results}, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2, ensure_ascii=False)

@mcp.tool()
async def sinta_detail_journal(url: str) -> str:
    """Lihat detail jurnal SINTA dari URL (contoh: /journals/123)"""
    try:
        full_url = f"{BASE}{url}" if url.startswith("/") else url
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as c:
            r = await c.get(full_url)
            soup = BeautifulSoup(r.text, "html.parser")
            data = {"url": full_url}
            texts = [t.strip() for t in soup.stripped_strings if t.strip() and len(t.strip()) > 3][:30]
            data["konten"] = texts
            return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    mcp.run()
