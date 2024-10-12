const multer = require("multer");
const path = require("path");

const storage = multer.diskStorage({
  destination: path.join(__dirname, "../../images"),
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  },
});

const upload = multer({ storage: storage });

exports.upload = upload.single("image");

exports.uploadFile = (req, res) => {
  req.getConnection((err, conn) => {
    if (err) return res.send(err);

    const type = req.file.mimetype;
    const name = req.file.originalname;

    conn.query(
      "INSERT INTO " + req.params.tabla + " set ?",
      [{ type, name }],
      (err, rows) => {
        console.log(
          err
            ? "Err INSERT INTO" + req.params.tabla + " " + err
            : req.params.tabla + ": Imagen agregada"
        );
        res.json(
          err
            ? { err: "Error al cargar la imagen" }
            : { msg: "Imagen cargada correctamente" }
        );
      }
    );
  });
};
