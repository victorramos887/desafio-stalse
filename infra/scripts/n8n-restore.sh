#!/usr/bin/env sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "Uso: $0 <caminho-do-backup.tar.gz>"
  exit 1
fi

BACKUP_FILE="$1"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if [ ! -f "$BACKUP_FILE" ]; then
  echo "Arquivo nao encontrado: $BACKUP_FILE"
  exit 1
fi

cd "$ROOT_DIR"

mkdir -p n8n_data

docker compose stop n8n >/dev/null 2>&1 || true
rm -rf n8n_data/*
tar -xzf "$BACKUP_FILE" -C "$ROOT_DIR"
docker compose up -d n8n

echo "Restore concluido usando: $BACKUP_FILE"
