# Retrieve a hero by ID
curl -X GET "http://127.0.0.1:8000/heroes/1"

# Create a new hero
curl -X POST "http://127.0.0.1:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
  "name": "Captain Strong",
  "secret_name": "John Power",
  "age": 35
}'

curl -X POST "http://127.0.0.1:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
  "name": "SuperBoy",
  "secret_name": "Paul budden",
  "age": 15
}'

curl -X POST "http://127.0.0.1:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
  "name": "RosyPosy",
  "secret_name": "Helen Mullen",
  "age": 28
}'

curl -X POST "http://127.0.0.1:8000/heroes/" \
-H "Content-Type: application/json" \
-d '{
  "name": "FoxBoy",
  "secret_name": "Fredric Tulson",
  "age": 22
}'

# Update a hero by ID
curl -X PUT "http://127.0.0.1:8000/heroes/1" \
-H "Content-Type: application/json" \
-d '{
  "age": 36
}'

# Delete a hero by ID
curl -X DELETE "http://127.0.0.1:8000/heroes/1"