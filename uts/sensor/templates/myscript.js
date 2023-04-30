// Initialize the chart data
var chartData = {
	labels: [],
	datasets: [{
		label: 'Data',
		data: [],
		backgroundColor: 'rgba(255, 99, 132, 0.2)',
		borderColor: 'rgba(255,99,132,1)',
		borderWidth: 1
	}]
};

// Get the chart canvas element and context
var ctx = document.getElementById('myChart').getContext('2d');

// Create the chart object
var myChart = new Chart(ctx, {
	type: 'line',
	data: chartData,
	options: {
		scales: {
			xAxes: [{
				type: 'time',
				time: {
					displayFormats: {
						second: 'h:mm:ss a'
					}
				}
			}]
		}
	}
});

// Function to add new data to the chart
function addData(timestamp, value) {
	myChart.data.labels.push(timestamp);
	myChart.data.datasets[0].data.push(value);
	myChart.update();
}

// Function to fetch new data from an API
function fetchData() {
	fetch('https://api.example.com/data')
		.then(function(response) {
			return response.json();
		})
		.then(function(data) {
			// Add the new data to the chart
			var timestamp = moment();
			var value = data.value;
			addData(timestamp, value);
		})
		.catch(function(error) {
			console.log(error);
		});
}

// Fetch new data every 5 seconds
setInterval(fetchData, 5000);
