#!/bin/bash

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

while IFS= read -r url; do
  timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

  # Extraire la dernière partie de l'URL
  last_part=$(basename "$url")
  if [[ -z "$last_part" || "$last_part" == "/" ]]; then
    last_part="accueil"
  fi

  output_file="results/${last_part}_${timestamp}.json"

  lighthouse "$url" \
    --only-categories=performance \
    --output=json \
    --output-path="$output_file" \
    --chrome-flags="--headless"

  echo "✅ Test terminé pour $url → $output_file"
done < urls.txt
