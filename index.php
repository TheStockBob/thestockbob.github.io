<?php
// Generate sample event data (replace this with your own logic)
$events = array(
    array(
        'title' => 'Event 1',
        'start' => '2024-04-15T10:00:00',
        'end' => '2024-04-15T12:00:00'
    ),
    array(
        'title' => 'Event 2',
        'start' => '2024-04-20',
        'end' => '2024-04-22'
    )
);

// Set the content type header to JSON
header('Content-Type: application/json');

// Output the event data as JSON
echo json_encode($events);
?>
