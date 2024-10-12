const express = require("express");

const app = express();

app.get("/", (req, res) => {
  if (req.query.user === "" || req.query.user === undefined) {
    console.log("No se encontró un usuario");
  } else {
    console.log(`El usuario es ${req.query.user}`);
  }

  res.send("Hello");
});

app.listen(3000);
console.log(`Server on port ${3000}`);
