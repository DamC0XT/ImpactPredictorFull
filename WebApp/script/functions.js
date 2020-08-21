let dateSelect = document.getElementById('select_date');

function dateChanger(){
    dateSelect.onchange = function(){
    
        date = dateSelect.value;
        alert(date);
    
    }
}