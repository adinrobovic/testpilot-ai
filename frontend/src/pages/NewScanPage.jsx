import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function NewScanPage() {
    const [url, setUrl] = useState("");
    const navigate = useNavigate();

    // Create a function for the button
    const handleStartScan = async () => {
        if (!url) {
            return;
        }

        const response = await fetch("http://127.0.0.1:8000/api/scans", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url })
        });

        const data = await response.json();
        
        navigate("/scanning", {
            state: { url }
        });
    };


    return(
        <div>
            <h1>New Scan</h1>
            <p>
                Scan your website for security risks, broken functionality, and accessibility issues.
                TestPilot AI turns technical findings into clear business impact and actionable next steps.   
            </p>

            <input 
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />

            <button onClick={handleStartScan}>
                Start Scan
            </button>

        </div>
    );
}