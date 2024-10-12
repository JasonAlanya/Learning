const express = require("express");
const mysql = require("mysql2");
const conn = require("express-myconnection");

const app = express();
app.set("port", process.env.PORT || 5000);

const dbconfig = {
  host: "localhost",
  port: "3306",
  user: "root",
  password: "J4son853",
  database: "management_system",
};

app.use(conn(mysql, dbconfig, "single"));

app.listen(app.get("port"), () => {
  console.log("Server running on port", app.get("port"));
});
