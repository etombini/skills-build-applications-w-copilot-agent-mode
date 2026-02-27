
const codespace = process.env.REACT_APP_CODESPACE_NAME;
console.log('REACT_APP_CODESPACE_NAME:', codespace);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
