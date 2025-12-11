//JS to create an alert box as secondary confirm of event deletion
document.addEventListener('DOMContentLoaded', function(){
    
    const deleteButtons = document.querySelectorAll('.delete-event-btn');

    deleteButtons.forEach(button=>{
        button.addEventListener('click',function(e){
            if(!confirm('Are you sure you want to delete this Event?')){
                e.preventDefault();
            };
        });
    });
});