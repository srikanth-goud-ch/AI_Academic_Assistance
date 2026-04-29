import { useState } from "react";
import { askQuestion } from "../api";

export default function ChatUI() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  const send = async () => {
    const res = await askQuestion({ question });

    setMessages([
      ...messages,
      { role: "user", text: question },
      { role: "bot", text: res.data.answer, sources: res.data.sources }
    ]);

    setQuestion("");
  };

  return (
    <div>
      <div>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.text}
            {m.sources && <div>Sources: {m.sources.join(", ")}</div>}
          </div>
        ))}
      </div>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={send}>Send</button>
    </div>
  );
}