<script>
    import svelteLogo from './assets/svelte.svg'
    import Counter from './lib/Counter.svelte'
</script>

<main>
    <h1>I15 Home System</h1>
    <button class="card">
        Temperature: 999
    </button>
    <button class="card">
        Humidity: 999
    </button>

    <button class="card">
        Motion: None
    </button>


    <p>
        I15 LTE Cat M1/NB1 Cellular Gateway for TI Launchpad
    </p>

    <p class="read-the-docs">
        Created by the Software Team
    </p>
</main>

<style>
    .logo {
        height: 6em;
        padding: 1.5em;
        will-change: filter;
        transition: filter 300ms;
    }

    .logo:hover {
        filter: drop-shadow(0 0 2em #646cffaa);
    }

    .logo.svelte:hover {
        filter: drop-shadow(0 0 2em #ff3e00aa);
    }

    .read-the-docs {
        color: #888;
    }
</style>
