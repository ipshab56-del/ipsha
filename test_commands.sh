curl -X GET "https://animated-goggles-pj47ppjpj7rrhj5.github.dev//api/students"

# B. Get One Student
curl -X GET "https://animated-goggles-pj47ppjpj7rrhj5.github.dev//api/students/1"

curl -X POST "https://animated-goggles-pj47ppjpj7rrhj5.github.dev//api/students" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "course": "Computer Science",
    "year": 2
  }'


.