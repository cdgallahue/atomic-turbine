rm -rf dist

echo "Creating dist.."
mkdir dist
mkdir dist/templates/

echo "Copying files.."
cp ./*.py ./dist/
cp ./requirements.txt ./dist/
cp ./runtime.txt ./dist/
cp ./templates/* ./dist/templates/
cp Procfile ./dist/
echo "Done."
