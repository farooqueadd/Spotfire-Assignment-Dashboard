
var css= ` .body {
    display: flex;
    justify-content: center;  /* Center horizontally */
    align-items: center;      /* Center vertically */
    height: 100vh;            /* Full screen height */
    margin: 0;
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    flex-direction: column;
}

.card-container {
    display: flex;
    justify-content: center;  /* Center the cards horizontally */
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;          /* Wrap on smaller screens */
    width: 100%;               /* Limit container width */
    max-width: 1200px;        /* Prevent excessive stretching */
    margin: auto;             /* Ensure it's centered */
}

.card {
    background-color: #fff;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 30px 20px;
    text-align: center;
    flex: 1;                  /* Grow to fill space */
    min-width: 110px;         /* Minimum width */
    max-width: 160px;         /* Maximum width */
	min-height: 100px;         /* Minimum width */
    max-height: 300px;         /* Maximum width */
}

.card .value {
    font-size: 2.5rem;
    font-weight: bold;
    color: #333;
}

.card .label {
    font-size: 1rem;
    color: #777;
}


            `;

		
$("<style/>").text(css).appendTo($("#maindiv"));