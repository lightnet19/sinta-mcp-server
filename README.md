# SINTA MCP Server

MCP server untuk mengakses data SINTA (Science and Technology Index) Indonesia.
Cek skor dosen, profil peneliti, dan peringkat institusi.

## Fitur
- 🔍 Cari profil dosen di SINTA
- 📊 Lihat skor dan detail dosen

## Instalasi

```bash
pip install sinta-mcp-server
```

## Konfigurasi MCP

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

## Tools
| Tool | Deskripsi |
|------|-----------|
| `sinta_search_dosen` | Cari dosen berdasarkan nama/NIDN |
| `sinta_detail_dosen` | Detail profil dosen dari URL SINTA |

## Lisensi
MIT
