$(document).ready(function() {

    $('#Details_TableID').DataTable({
        "pageLength": 5
    });


    $('#Details_TableID').on('click', '.SeeJobiDCred', function(e) {



        console.log($(this).attr("value"))



        Id = $(this).attr("value");
        console.log(e)
        debugger;
        window.open('http://127.0.0.1:8000/admin/website/customjobinformations/' + Id + '/change/', '_self');
        //'http://127.0.0.1:8000/admin/website/customjobinformations/'+ID+'/change/'

        return false;
    });

    $('#Details_TableID').on('click', '.SeeJobiD', function(e) {

        console.log($(this).attr("value"));
        Id = $(this).attr("value");

        debugger;
        url = 'http://127.0.0.1:8000/createcustomjob/?ID=' + Id
        console.log(url)
        window.open('http://127.0.0.1:8000/createcustomjob/?ID=' + Id, '_self');

        return false;

    });

    $('#Details_TableID').on('click', '.tempclass2', function(e) {

        console.log($(this).attr("value"));
        Id = $(this).attr("value");

        debugger;
        $.ajax({
            type: "GET",
            url: "/RunCustomJobNow/",
            data: {
                ID: Id

            },

            dataType: 'json',

            success: function(data) {
                console.log(data)
                //$('#LoaderID').css({"display":"None"})
                //$('#MainContentsID').css({"display":"Block"})

            }

        });

    });


    $('#Details_TableID').on('click', '.tempclass3', function(e) {

        $('#LoaderID').css({
            "display": "Block"
        })
        $('#MatHistoryID').css({
            "visibility": "hidden"
        })
        $('#Historydivid').css({
            "display": "none"
        })
        $('#MatHistoryID_wrapper').css({
            "visibility": "hidden"
        })

        console.log($(this).attr("value"))

        jonIDname = $(this).attr("value");
        console.log('jonIDname ' + jonIDname)

        $.ajax({
            type: "GET",
            url: "/SeeCustomHistory/",
            data: {
                JobID: jonIDname,
            },

            dataType: 'json',

            success: function(data) {
                if ($.fn.DataTable.isDataTable("#MatHistoryID")) {
                    $('#MatHistoryID').DataTable().clear().destroy();
                    console.log('in destroy')
                }

                var trHTML = ''
                console.log('--kkkkkk------')
                console.log(data['history_data'])
                li = data['history_data']
                for (i = 0; i < li.length; i++) {
                    //console.log(li[i].JobID)
                    trHTML += '<tr><td>' + li[i].JobID + '</td><td>' + li[i].JobName + '</td><td>' + li[i].StartTime + '</td><td>' + li[i].EndTime + '</td><td>' + li[i].Sche_or_Manu + '</td><td>' + li[i].Status + '</td><td>' + li[i].description + '</td></tr>'
                }
                $("#MatHistoryIDbody").empty();
                $('#MatHistoryIDbody').append(trHTML);

                $('#Historydivid').css({
                    "display": ""
                })
                $('#MatHistoryID').css({
                    "visibility": "visible"
                })
                $('#LoaderID').css({
                    "display": "none"
                })
                $('#MatHistoryID_wrapper').css({
                    "visibility": "visible"
                })

                //////



                ////

                $('#MatHistoryID').DataTable({

                    "pageLength": 5,
                    columnDefs: [{
                        targets: 6,
                        render: $.fn.dataTable.render.ellipsis(50)
                    }]
                });


            }
        });

    });


});




function History_Table_Search(No) {


    Arr_of_Id = ['DetailSearchId_JobID', 'DetailSearchId_JobName', 'DetailSearchId_StartTime', 'DetailSearchId_EndTime', 'DetailSearchId_Status']

    var InputID = Arr_of_Id[No]
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(InputID);
    filter = input.value.toUpperCase();
    table = document.getElementById("MatHistoryID");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[No];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function Details_Table_Search(No) {


    Arr_of_Id = ['DetailsSearchTable_JobName', 'DetailsSearchTable_Timing', 'DetailsSearchTable_Timing_days', 'DetailsSearchTable_Enable', 'DetailsSearchTable_LastModifiedby']

    var InputID = Arr_of_Id[No]
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(InputID);
    filter = input.value.toUpperCase();
    table = document.getElementById("Details_TableID");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[No];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


$(document).ready(function() {

    $('#RefreshPage').on('click', function(e) {
        // show Loading Icon
        $('#LoaderID').css({
            "display": "Block"
        })
        $('#MainContentsID').css({
            "display": "none"
        })
        e.preventDefault();

        $.ajax({
            synch: 'true',
            type: 'GET',
            url: 'http://127.0.0.1:8000/CustomJobSee/',
            success: function(data) {
                console.log(data)
                $('#bodycontentid').html(data);
                $('#LoaderID').css({
                    "display": "None"
                })
                $('#MainContentsID').css({
                    "display": "Block"
                })
            }
        }); //End Ajax
    });
});

$(document).ready(function() {
    $('#Closeid').on('click', function() {
        $('#myModal').css({
            "display": "None"
        })

    });
});

window.onclick = function(event) {
    //if (event.target == modal) {
    console.log(event.target.id)
    if (event.target.id == 'myModal') {
        $('#myModal').css({
            "display": "None"
        })

    }
    //}
}