function view_all() {
    $.ajax({
        url: "",
        type: "get",
        success: function (response) {
            $('#contenido_actualizado').html(response);            
        },
        error: function (error) {
            console.log('error');
        }
    });
}


function register() {
    $.ajax({
        data: $('#form_creation').serialize(),
        url: $('#form_creation').attr('action'),
        type: $('#form_creation').attr('method'),
        success: function (response) {
            view_all();
        },
        error: function (error) {
            console.log('error')
        }
    })
}





$('#delete').on("click", function (e) {
    e.preventDefault();
    const delete_id = $('#delete').val()        
    $.ajax({
        url: "delete/" + delete_id,
        type: "GET",
        dataType: "json",
        success: function (response) {
            view_all();
            
        },
        error: function (response) {
            console.log("error")
        }

    })
})

$('#delete_two').on("click", function (e) {
    e.preventDefault();
    const delete_id_two = $('#delete_two').val()        
    $.ajax({
        url: "delete/" + delete_id_two,
        type: "GET",
        dataType: "json",
        success: function (response) {
            view_all();                
        },
        error: function (response) {
            console.log("error")
        }

    })
})

$('#delete_there').on("click", function (e) {
    e.preventDefault();
    const delete_id = $('#delete_there').val()        
    $.ajax({
        url: "delete/" + delete_id,
        type: "GET",
        dataType: "json",
        success: function (response) {
            view_all();                
        },
        error: function (response) {
            console.log("error")
        }

    })
})
