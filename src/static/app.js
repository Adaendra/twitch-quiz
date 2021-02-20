new Vue({
    el: '#components-demo',
    template: `
    <div id="routes">
        <h1>Home Page</h1>
          <p>Welcome home!</p>
          <ul>
             <li><router-link to="/contact">Contact</router-link></li>
             <li><router-link to="/faq">FAQ</router-link></li>
          </ul>
        <button-counter></button-counter>
    </div>
    `
    })

