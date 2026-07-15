# Contributing to SINTA MCP Server

Terima kasih ingin berkontribusi! 🎉

## Cara Berkontribusi

### 1. Laporkan Bug / Saran Fitur
Buka [Issues](https://github.com/lightnet19/sinta-mcp-server/issues) dan gunakan template yang tersedia.

### 2. Pull Request
```bash
# Fork repo
git clone https://github.com/[username]/sinta-mcp-server.git
cd sinta-mcp-server

# Buat branch baru
git checkout -b feat/fitur-baru

# Install dependencies
pip install -e .

# Buat perubahan
# ...

# Commit
git add .
git commit -m "feat: deskripsi perubahan"

# Push
git push origin feat/fitur-baru
```

Buat Pull Request ke branch `main`.

### 3. Development Setup
```bash
pip install -e .
python3 -m sinta_mcp_server
```

### Pedoman
- Ikuti struktur kode yang sudah ada
- Gunakan type hints Python
- Tambahkan docstring pada fungsi baru
- Test perubahan sebelum PR
- Gunakan Conventional Commits (`feat:`, `fix:`, `docs:`, dll)

## Lisensi
MIT - dengan berkontribusi, Anda setuju perubahan Anda dilisensikan MIT.
