/*!
    * Start Bootstrap - SB Admin v6.0.0 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    (function($) {
    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });

    $('.btn').on('click', function() {
        var url = $("input#url").val();
        $.ajax({
            url: "http://localhost:8080/scraper-api/getAll/",
            type: "GET",
            data: {
              url: url
            },
            success: function(res) {
                $("#message").append("<div class='alert alert-success col-xl'>")
                $("#message > .alert-success").html("<strong>Los datos fueron cargados exitosamente " + url + "</strong>");
                $("#message").append("</div>");
                // Data
                $("#title").append(res.title);
                $("#total_sentences").append(res.results.total_sentences)
                for (var i = 0; i < 2; i++) {
                    $("#news").append("<p style='padding: 1%'>" + res.results.sentences[i] + "</p>" )
                }
                $(".table-bordered").append("<thead><tr><th>Índice</th><th>Data</th></tr></thead><tfoot><tr><th>Índice</th><th>Data</th></tr></tfoot>");
                $(".table-bordered").append("<tbody class='table-content'>");
                for (var i = 0; i < res.results.sentences.length; i++) {
                    var indice = i + 1 
                    $(".table-content").append("<tr><td>" + indice + "</td><td>" + res.results.sentences[i] + "</td></tr>")
                }
                $(".table-bordered").append("</tbody>");
            }
        })
    });
})(jQuery);
