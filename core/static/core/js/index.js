let contadorClicks = 0;

$(document).ready(function () {
  $("#id_nombreUsuario").focusout(function () {
    console.log("Sali del foco nombre de usuario registro");

    if (
      $("#id_nombreUsuario")[0].value == "" ||
      $("#id_nombreUsuario")[0].value.trim() == "" ||
      $("#id_nombreUsuario")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertNonmbreUsuarioRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertNonmbreUsuarioRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_correoUsuario").focusout(function () {
    console.log("Sali del foco correo registro");

    if (
      $("#id_correoUsuario")[0].value == "" ||
      $("#id_correoUsuario")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertCorreoRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertCorreoRegistro")[0]
        .classList.add("hide");
      console.log("2");
      let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
      if (!regexEmail.test(id_correoUsuario.value)) {
        document
          .getElementsByName("joinusNameAlertCorreoFormatoRegistro")[0]
          .classList.remove("hide");
      } else {
        document
          .getElementsByName("joinusNameAlertCorreoFormatoRegistro")[0]
          .classList.add("hide");
      }
    }
  });

  $("#id_nombre").focusout(function () {
    console.log("Sali del foco nombre persona registro");

    if (
      $("#id_nombre")[0].value == "" ||
      $("#id_nombre")[0].value.trim() == "" ||
      $("#id_nombre")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertNonmbreRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertNonmbreRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_apellidoPaterno").focusout(function () {
    console.log("Sali del foco apellido paterno registro");

    if (
      $("#id_apellidoPaterno")[0].value == "" ||
      $("#id_apellidoPaterno")[0].value.trim() == "" ||
      $("#id_apellidoPaterno")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertApellidoPaternoRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertApellidoPaternoRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_apellidoMaterno").focusout(function () {
    console.log("Sali del foco apellido materno usuario registro");

    if (
      $("#id_apellidoMaterno")[0].value == "" ||
      $("#id_apellidoMaterno")[0].value.trim() == "" ||
      $("#id_apellidoMaterno")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertApellidoMaternoRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertApellidoMaternoRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_direccion").focusout(function () {
    console.log("Sali del foco direccion registro");

    if (
      $("#id_direccion")[0].value == "" ||
      $("#id_direccion")[0].value.trim() == "" ||
      $("#id_direccion")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertDireccionRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertDireccionRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_passwordUsuario").focusout(function () {
    console.log("Sali del foco password usuario registro");

    if (
      $("#id_passwordUsuario")[0].value == "" ||
      $("#id_passwordUsuario")[0].value.trim() == "" ||
      $("#id_passwordUsuario")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertContraseñaRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertContraseñaRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#comentarios").focusout(function () {
    console.log("Sali del foco comentario");

    if (
      $("#comentarios")[0].value == "" ||
      $("#comentarios")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertComentario")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertComentario")[0]
        .classList.add("hide");
      console.log("mmmmmm");
    }
  });

  $("#joinusNameLogin").focusout(function () {
    console.log("Sali del foco nombre");

    if (
      $("#joinusNameLogin")[0].value == "" ||
      $("#joinusNameLogin")[0].value.trim() == "" ||
      $("#joinusNameLogin")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertNameLogin")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertNameLogin")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#joinusNamePwdLogin").focusout(function () {
    console.log("Sali del foco nombre");

    if (
      $("#joinusNamePwdLogin")[0].value == "" ||
      $("#joinusNamePwdLogin")[0].value.trim() == "" ||
      $("#joinusNamePwdLogin")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertPwdLogin")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertPwdLogin")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#joinusNamePwdRegistro").focusout(function () {
    console.log("Sali del foco nombre");

    if (
      $("#joinusNamePwdRegistro")[0].value == "" ||
      $("#joinusNamePwdRegistro")[0].value.trim() == "" ||
      $("#joinusNamePwdRegistro")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertPwdRegistro")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertPwdRegistro")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_nombreContacto").focusout(function () {
    console.log("Sali del foco nombre contacto");

    if (
      $("#id_nombreContacto")[0].value == "" ||
      $("#id_nombreContacto")[0].value.trim() == "" ||
      $("#id_nombreContacto")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertNameContacto")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertNameContacto")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#id_correoContacto").focusout(function () {
    console.log("Sali del foco correo contacto");

    if (
      $("#id_correoContacto")[0].value == "" ||
      $("#id_correoContacto")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertCorreoContacto")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertCorreoContacto")[0]
        .classList.add("hide");
      console.log("2");
      let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
      if (!regexEmail.test(id_correoContacto.value)) {
        document
          .getElementsByName("joinusNameAlertCorreoFormatoContacto")[0]
          .classList.remove("hide");
      } else {
        document
          .getElementsByName("joinusNameAlertCorreoFormatoContacto")[0]
          .classList.add("hide");
      }
    }
  });

  $("#id_comentarioContacto").focusout(function () {
    console.log("Sali del foco comentario contacto");

    if (
      $("#id_comentarioContacto")[0].value == "" ||
      $("#id_comentarioContacto")[0].value.trim() == "" ||
      $("#id_comentarioContacto")[0].value == null
    ) {
      document
        .getElementsByName("joinusNameAlertNameComentarioContacto")[0]
        .classList.remove("hide");
    } else {
      document
        .getElementsByName("joinusNameAlertNameComentarioContacto")[0]
        .classList.add("hide");
      console.log("1");
    }
  });

  $("#formulariologin").submit(function (event) {
    console.log("Formulario enviado");
    event.preventDefault();
  });

  $("#button_api_animales").click(function () {
    $.get(`https://cat-fact.herokuapp.com/facts`, function (data) {
      console.log(data);

      $("#datos_animales").append(
        "<ul><li>" +
          data[0].text +
          "</li><li>" +
          data[1].text +
          "</li><li>" +
          data[2].text +
          "</li><li>" +
          data[3].text +
          "</li></ul>"
      );
      console.log(data[0].text);
      console.log(data[1].text);
      console.log(data[2].text);
      console.log(data[3].text);
    });
  });
});
