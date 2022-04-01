document.addEventListener("DOMContentLoaded", function() {

    var calendarEl = document.getElementById("calendar");

    var calendar   = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
        selectable    : true,
        now           : "2020-09-07",
        editable      : false, // disable draggable events
        aspectRatio   : 1.8,
        scrollTime    : "00:00", // undo default 6am scrollTime
        headerToolbar : {
            left: "today prev,next",
            center: "title",
            right: "timelineDay,timelineThreeDays,timeGridWeek,dayGridMonth",
        },
        initialView   : "dayGridMonth",
        views         : {
            timelineThreeDays: {
                type: "timeline",
                duration: { days: 3 },
                buttonText: "3 days"
            }
        },
        events: [
            { id: '1', start: "2020-09-07T02:00:00", end: "2020-09-07T07:00:00", title: "event 1" },
            { id: '2', start: "2020-09-07T05:00:00", end: "2020-09-07T22:00:00", title: "event 2" },
            { id: '3', start: "2020-09-06", end: "2020-09-08", title: "event 3" },
            { id: '4', start: "2020-09-07T03:00:00", end: "2020-09-07T08:00:00", title: "event 4" },
            { id: '5', start: "2020-09-07T00:30:00", end: "2020-09-07T02:30:00", title: "event 5" }
        ]
    });

    calendar.render();

});