
# Capstone - PlantRO

An application to determine the crop rotation suitable for planting based on soil Ph, rainfall, and soil content.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Capstone-Ps109/capstone-api.git
```

Go to the project directory

```bash
  cd auth-api
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## API Reference

#### Register User
- URL : 
  - `/auth/register`
- Method : 
  - `POST`
- Request Body :
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | Your name |
| `email` | `string` | Must be unique |
| `password` | `string` | Must be at least 8 characters |
- Response
  - Success
  ```json
  {
      "message": "Registrasi berhasil",
      "userId": "vhL4OfKcskx550CdIdB3"
  }
  ```
  - Empty name
  ```json
  {
      "error": "Nama harus diisi"
  }
  ```
  - Empty email
  ```json
  {
    "error": "Email harus diisi, Email tidak valid"
  }
  ```
  - Lack of @ sign in email
  ```json
  {
    "error": "Email tidak valid"
  }
  ```
  - Password less than 8 character
  ```json
  {
    "error": "Password minimal 8 karakter"
  }
  ```
  - Email already registered
  ```json
  {
    "error": "Email sudah terdaftar"
  }
  ```

#### Login User
- URL : 
  - `/auth/login`
- Method : 
  - `POST`
- Request Body :
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` |  |
| `password` | `string` |  |
- Response
  - Success
  ```json
  {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ2aEw0T2ZLY3NreDU1MENkSWRCMyIsImlhdCI6MTczMzcxNjgxNiwiZXhwIjoxNzMzODAzMjE2fQ._RunFkOuqSueEgmzz9blqq1ILx9IK8PyhuF8L7hx0Co",
      "user": {
          "id": "vhL4OfKcskx550CdIdB3",
          "name": "Nurhidayat",
          "email": "dayatdays@gmail.com"
      }
  }
  ```
  - Wrong email or password
  ```json
  {
    "error": "Email atau password salah"
  }
  ```

#### Get Profile
- URL : 
  - `/auth/profile`
- Method : 
  - `GET`
- Headers :
| Key | Value     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Bearer <token>` |  |
- Response
  - Success
  ```json
  {
      "id": "vhL4OfKcskx550CdIdB3",
      "name": "Nurhidayat",
      "email": "dayatdays@gmail.com",
      "createdAt": {
          "_seconds": 1733716553,
          "_nanoseconds": 132000000
      }
  }
  ```
  - Wrong token
  ```json
  {
    "error": "Token tidak valid"
  }
  ```
  - No tokens
  ```json
  {
    "error": "Tidak ada token, otorisasi ditolak"
  }
  ```
  - No user data
  ```json
  {
    "error": "Pengguna tidak valid"
  }
  ```

#### Logout User
- URL : 
  - `/auth/logout`
- Method : 
  - `POST`
- Headers :
| Key | Value     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Bearer <token>` |  |
- Response
  - Success
  ```json
  {
      "message": "Logout berhasil",
      "info": "Token telah di-blacklist"
  }
  ```
  - No user data
  ```json
  {
    "error": "Pengguna tidak valid"
  }
  ```
  - Wrong token
  ```json
  {
    "error": "Token tidak valid"
  }
  ```

