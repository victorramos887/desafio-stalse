#!/usr/bin/env sh
set -eu

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
N8N_ROOT_DIR="$ROOT_DIR/../n8n"
N8N_DATA_DIR="$N8N_ROOT_DIR/data"
BACKUP_DIR="$N8N_ROOT_DIR/backups"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT_FILE="$BACKUP_DIR/n8n_data-$STAMP.tar.gz"
WORKFLOWS_FILE="$BACKUP_DIR/workflows-$STAMP.json"
CREDENTIALS_FILE="$BACKUP_DIR/credentials-decrypted-$STAMP.json"
N8N_CONTAINER="mini-inbox-n8n"

mkdir -p "$N8N_DATA_DIR"
mkdir -p "$BACKUP_DIR"

cd "$N8N_ROOT_DIR"

tar -czf "$OUT_FILE" data

echo "Backup criado: $OUT_FILE"

# Export workflows for portable restore across machines.
if docker ps --format '{{.Names}}' | grep -qx "$N8N_CONTAINER"; then
	if docker exec "$N8N_CONTAINER" n8n export:workflow --all --output=/home/node/.n8n/workflows-export.json >/dev/null 2>&1; then
		cp "$N8N_DATA_DIR/workflows-export.json" "$WORKFLOWS_FILE"
		rm -f "$N8N_DATA_DIR/workflows-export.json"
		echo "Export JSON workflows: $WORKFLOWS_FILE"
	else
		echo "Aviso: nao foi possivel exportar workflows em JSON."
	fi

	# Decrypted credentials allow recovery even with a different encryption key.
	if docker exec "$N8N_CONTAINER" n8n export:credentials --all --decrypted --output=/home/node/.n8n/credentials-decrypted-export.json >/dev/null 2>&1; then
		cp "$N8N_DATA_DIR/credentials-decrypted-export.json" "$CREDENTIALS_FILE"
		rm -f "$N8N_DATA_DIR/credentials-decrypted-export.json"
		echo "Export JSON credenciais (decrypted): $CREDENTIALS_FILE"
	else
		echo "Info: sem credenciais para exportar (ou export indisponivel)."
	fi
else
	echo "Info: container $N8N_CONTAINER nao esta rodando; backup JSON nao foi gerado."
fi
