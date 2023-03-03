<script>
    import svelteLogo from './assets/svelte.svg'
    import Counter from './lib/Counter.svelte'

    let temperature;
    let motion;
    let humidity;

    function getTempFromBackend() {
        fetch("./temp")
            .then(d => d.text())
            .then(d => (temperature = d));

        setTimeout(getTempFromBackend, 1000);
    }


    function getMotionFromBackend() {
        fetch("./motion")
            .then(d => d.text())
            .then(d => (motion = d));

        setTimeout(getMotionFromBackend, 1000);
    }

    function getHumidityFromBackend() {
        fetch("./humidity")
            .then(d => d.text())
            .then(d => (humidity = d));

        setTimeout(getHumidityFromBackend, 1000);
    }

    getHumidityFromBackend();
    getTempFromBackend();
    getMotionFromBackend();


</script>

<main>
    <h1>I15's Custom TM4C Home System</h1>

    <h2>
        Temperature: {temperature} Degrees Fahrenheit
    </h2>
    <h2>
        Motion Reading: {motion}
    </h2>
    <h2>
        Humidity Level: {humidity} %rh
    </h2>

    <p>
        Check out <a href="https://github.com/SkyRocket456/TM4CSite" target="_blank" rel="noreferrer">the
        repository </a> for
        the website here!
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
