<script>
    let motion;
    let light;
    let moisture;

    let pin_type = "PA";
    let pin_number = "2";
    let selectedOption = "2";

    let pins = [
        {value: "2", label: "2"},
        {value: "3", label: "3"},
        {value: "4", label: "4"},
        {value: "5", label: "5"},
        {value: "6", label: "6"},
        {value: "7", label: "7"},
    ];

    let signal = "Digital";
    let io = "Input";

    function getMotionFromBackend() {
        fetch("./motion")
            .then(d => d.text())
            .then(d => (motion = d));

        setTimeout(getLightFromBackend, 1000);
    }


    function getLightFromBackend() {
        fetch("./light")
            .then(d => d.text())
            .then(d => (light = d));

        setTimeout(getMotionFromBackend, 1000);
    }

    function getMoistureFromBackend() {
        fetch("./moisture")
            .then(d => d.text())
            .then(d => (moisture = d));

        setTimeout(getMoistureFromBackend, 1000);
    }

    function handlePinType(event) {
        pin_type = event.target.value;

        if (pin_type === "PA") {
            pins = [
                {value: "2", label: "2"},
                {value: "3", label: "3"},
                {value: "4", label: "4"},
                {value: "5", label: "5"},
                {value: "6", label: "6"},
                {value: "7", label: "7"},
            ];

            selectedOption = "2"
            pin_number = "2"
        }

        if (pin_type === "PB") {
            pins = [
                {value: "0", label: "0"},
                {value: "1", label: "1"},
                {value: "2", label: "2"},
                {value: "3", label: "3"},
                {value: "4", label: "4"},
                {value: "5", label: "5"},
                {value: "6", label: "6"},
                {value: "7", label: "7"},
            ];

            selectedOption = "0"
            pin_number = "0"
        }

        if (pin_type === "PC") {
            pins = [
                {value: "0", label: "0"},
                {value: "1", label: "1"},
                {value: "2", label: "2"},
                {value: "3", label: "3"},
                {value: "4", label: "4"},
                {value: "5", label: "5"},
            ];

            selectedOption = "0"
            pin_number = "0"
        }
    }

    function sendInfo() {
        console.log(pin_type)
        console.log(pin_number)
        console.log(signal)
        console.log(io)
        // Send a POST request to the Django server
        fetch("./pin_control", {
            method: 'POST',
            withCredentials: true,
            mode: "cors",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    pin_type: pin_type,
                    pin_number: pin_number,
                    signal: signal,
                    io: io
                })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)
            })
            .catch(error => {
                console.log(error)
            });
    }

    getMoistureFromBackend();
    getLightFromBackend();
    getLightFromBackend();
</script>

<main>
    <h1 class="title">I15's Custom TM4C LTE Multi-Purpose System</h1>

    <div class="grid">
        <div class="grid-item">
            <h2>
                Motion Reading: {motion} Detected
            </h2>
            <h2>
                Light Reading: {light}%
            </h2>
            <h2>
                Moisture Level: {moisture}%
            </h2>
        </div>
        <div class="grid-item">
            <label class="pin-menu-item">Which pin would you like to control?</label>
            <select on:change={handlePinType}>
                <option value="PA">PA</option>
                <option value="PB">PB</option>
                <option value="PC">PC</option>
            </select>
            <select bind:value={selectedOption} on:change={(e) => (pin_number = e.target.value)}>
                {#each pins as option}
                    <option value={option.value}>{option.label}</option>
                {/each}
            </select>

            <br><br>

            <label class="pin-menu-item">Digital or Analog?</label>
            <select on:change={(e) => (signal = e.target.value)}>
                <option value="Digital">Digital</option>
                <option value="Analog">Analog</option>
            </select>

            <br><br>

            <label class="pin-menu-item">Input or Output?</label>
            <select on:change={(e) => (io = e.target.value)}>
                <option value="Input">Input</option>
                <option value="Output">Output</option>
            </select>

            <br><br>

            <button on:click={sendInfo}>
                SEND
            </button>
        </div>
    </div>


    <p>
        Check out <a href="https://github.com/SkyRocket456/TM4CSite" target="_blank" rel="noreferrer">the
        repository </a> for the website here!
    </p>

    <p class="read-the-docs">
        Created by the I15 Software Team
    </p>

</main>

<style>
    .read-the-docs {
        color: #888;
    }
</style>
