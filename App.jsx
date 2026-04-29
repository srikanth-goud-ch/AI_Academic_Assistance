import ChatUI from "./components/ChatUI";
import UploadPanel from "./components/UploadPanel";

function App() {
  return (
    <div>
      <h1>AI Academic Assistant</h1>
      <UploadPanel />
      <ChatUI />
    </div>
  );
}

export default App;