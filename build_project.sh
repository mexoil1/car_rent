cd car_rent
docker build -t grigoleg/car_rent_backend .
cd ../gateway
docker build -t grigoleg/car_rent_gateway .
docker push grigoleg/car_rent_backend
docker push grigoleg/car_rent_gateway