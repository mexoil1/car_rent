if [ -f .env ]; then
    echo "Загрузка переменных из файла .env..."
    source .env
fi

echo "Запуск MinIO..."
MINIO_ROOT_USER=$MINIO_ACCESS_KEY MINIO_ROOT_PASSWORD=$MINIO_SECRET_KEY minio server ~/mnt/data --console-address ":9001" &

echo "Запуск сервера..."
python car_rent/manage.py runserver
wait
