# SINTA MCP Server 🎯

MCP server untuk mengakses **Science and Technology Index (SINTA)** Indonesia.
Cek skor dosen, profil peneliti, akreditasi jurnal, dan publikasi ilmiah — langsung dari AI assistant Anda!

## ✨ Fitur

| Tool | Deskripsi | Parameter |
|------|-----------|-----------|
| 🔍 `sinta_search_dosen` | Cari profil dosen di SINTA | `query` (nama/NIDN) |
| 👤 `sinta_detail_dosen` | Detail profil dosen (skor, publikasi) | `url` (URL SINTA) |
| 📰 `sinta_search_jurnal` | Cari jurnal terindeks SINTA | `query`, `akreditasi` (S1-S6) |
| 📖 `sinta_detail_journal` | Detail jurnal SINTA | `url` (URL jurnal) |
| 📄 `sinta_search_artikel` | Cari artikel/publikasi di SINTA | `query`, `tahun_from`, `tahun_to` |

### Contoh Penggunaan

**Cari dosen:**
```
sinta_search_dosen(query="fuad al fajri")
```

**Cari jurnal S2:**
```
sinta_search_jurnal(query="pendidikan", akreditasi="S2")
```

**Cari artikel:**
```
sinta_search_artikel(query="metakognisi pendidikan dasar")
```

> ⚠️ **Catatan:** SINTA menggunakan JavaScript rendering. Untuk hasil pencarian artikel yang lebih akurat, gunakan **Semantic Scholar**, **OpenAlex**, atau **CrossRef** MCP server.

## 🔧 Instalasi

```bash
pip install sinta-mcp-server
```

## ⚙️ Konfigurasi MCP

Tambahkan ke config MCP client Anda (Claude Desktop, Hermes, dll):

```json
{
  "mcpServers": {
    "sinta": {
      "command": "python3",
      "args": ["-m", "sinta_mcp_server"]
    }
  }
}
```

## 🏗️ Arsitektur

Server ini menggunakan **FastMCP**, **httpx**, dan **BeautifulSoup** untuk mengakses data dari SINTA:

- **Sumber data:** [sinta.kemdiktisaintek.go.id](https://sinta.kemdiktisaintek.go.id)
- **Runtime:** Python ≥3.10
- **Dependencies:** fastmcp, httpx, beautifulsoup4, lxml

## 📋 Pengembangan

```bash
git clone https://github.com/lightnet19/sinta-mcp-server.git
cd sinta-mcp-server
pip install -e .
python3 -m sinta_mcp_server
```

## 🔗 Integrasi dengan MCP Server Lain

SINTA MCP bekerja paling baik bersama MCP server lain untuk riset:

| MCP Server | Kegunaan |
|---|---|
| **OpenAlex** | 250M+ publikasi global |
| **Semantic Scholar** | Paper search + TLDR |
| **CrossRef** | DOI lookup |
| **ORCID** | Profil peneliti global |
| **arXiv** | Preprint + topic alerts |

## 📄 Lisensi

MIT © 2026 Fuad Al Fajri
