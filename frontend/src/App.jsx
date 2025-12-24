import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [sentiment, setSentiment] = useState("");
  const [error, setError] = useState("");

  const predictSentiment = async () => {
    if (!text.trim()) return;

    try {
      setError(""); // reset previous error
      setSentiment("...Predicting");

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error(`Backend returned ${response.status}`);
      }

      const data = await response.json();
      setSentiment(data.sentiment);
    } catch (err) {
      setError("Failed to get sentiment. Check backend.");
      setSentiment("");
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h2>Twitter Sentiment Analysis</h2>

      <textarea
        rows="4"
        cols="50"
        placeholder="Enter tweet text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br /><br />

      <button onClick={predictSentiment}>Predict Sentiment</button>

      <br /><br />

      {sentiment && <h3>Sentiment: {sentiment}</h3>}
      {error && <h4 style={{ color: "red" }}>{error}</h4>}
    </div>
  );
}

export default App;


