#!/bin/bash

LH_USERNAME=""
LH_PASSWORD=""

# Function to display usage
usage() {
  echo "Usage: $0 [options]"
  echo "Options:"
  echo "  -u, --username <username>  Username for Basic Authentication"
  echo "  -p, --password <password>  Password for Basic Authentication"
  echo "  -h, --help                 Display this help message"
  exit 1
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
    -u|--username) LH_USERNAME="$2"; shift ;;
    -p|--password) LH_PASSWORD="$2"; shift ;;
    -h|--help) usage ;;
    *) echo "Unknown parameter passed: $1"; usage ;;
  esac
  shift
done

# Prepare Authorization header if username is provided
if [ -n "$LH_USERNAME" ]; then
  auth_string=$(echo -n "$LH_USERNAME:$LH_PASSWORD" | base64)
  export LH_AUTH_HEADER="Authorization: Basic $auth_string"
fi

# Vérification de l'existence du fichier
if [ ! -f urls.txt ]; then
  echo "❌ Erreur : le fichier 'urls.txt' est introuvable."
  exit 1
fi

# Compter le nombre d'URLs
url_count=$(wc -l < urls.txt | tr -d ' ')
estimated_time=$((url_count * 15))

echo "✅ Fichier 'urls.txt' trouvé avec $url_count URL(s)."
echo "⏳ Estimation du temps total : environ $estimated_time secondes (~$((estimated_time / 60)) minutes)."
echo "🚀 Début des tests Lighthouse..."

mkdir -p results

while IFS= read -r url || [[ -n "$url" ]]; do
  # Skip if line starts with # (comment)
  if [[ "$url" == \#* ]]; then
    continue
  fi
  timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

  # Extraire la dernière partie de l'URL
  last_part=$(basename "$url")
  if [[ -z "$last_part" || "$last_part" == "/" ]]; then
    last_part="accueil"
  fi

  output_file="results/${last_part}_${timestamp}.json"

  if [ -n "$LH_AUTH_HEADER" ]; then
    lighthouse "$url" \
      --only-categories=performance \
      --output=json \
      --output-path="$output_file" \
      --chrome-flags="--headless" \
      --extra-headers "{\"Authorization\": \"Basic $auth_string\"}"
  else
    lighthouse "$url" \
      --only-categories=performance \
      --output=json \
      --output-path="$output_file" \
      --chrome-flags="--headless"
  fi

  echo "✅ Test terminé pour $url → $output_file"
done < urls.txt
