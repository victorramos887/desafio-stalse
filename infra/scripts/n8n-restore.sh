#!/usr/bin/env sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "Uso: $0 <caminho-do-backup.tar.gz>"
  exit 1
fi

BACKUP_FILE="$1"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
N8N_ROOT_DIR="$ROOT_DIR/../n8n"
N8N_DATA_DIR="$N8N_ROOT_DIR/data"

if [ ! -f "$BACKUP_FILE" ]; then
  echo "Arquivo nao encontrado: $BACKUP_FILE"
  exit 1
fi

mkdir -p "$N8N_ROOT_DIR"
cd "$N8N_ROOT_DIR"

mkdir -p "$N8N_DATA_DIR"

cd "$ROOT_DIR"
docker compose stop n8n >/dev/null 2>&1 || true
rm -rf "$N8N_DATA_DIR"/*
tar -xzf "$BACKUP_FILE" -C "$N8N_ROOT_DIR"
docker compose up -d n8n

echo "Restore concluido usando: $BACKUP_FILE"
