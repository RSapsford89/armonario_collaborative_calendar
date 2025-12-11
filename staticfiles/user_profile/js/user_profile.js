//JS to create an alert box as secondary confirm leaving a Group
document.addEventListener('DOMContentLoaded', function () {

    const deleteButtons = document.querySelectorAll('.leave-group-btn');

    deleteButtons.forEach((button) => {
        button.addEventListener('click', function (e) {
            if (!confirm('Are you sure you want to leave this Group?')) {
                e.preventDefault();
            }
        });
    });
});