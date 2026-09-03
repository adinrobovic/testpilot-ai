import { Link } from "react-router-dom";

export default function Navbar() {
    return(
        <div>
            <h1>TestPilot AI</h1>
            <Link to="/home">Home</Link>
            <Link to="/history">History</Link>
        </div>
    )
}