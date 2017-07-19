rm -rf dist

echo "Creating dist.."
mkdir dist

echo "Copying files.."
cp ./*.py ./dist/
cp ./requirements.txt ./dist/
cp ./runtime.txt ./dist/

echo "Done."
