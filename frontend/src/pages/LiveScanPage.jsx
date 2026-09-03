import { useLocation } from "react-router-dom";
import FindingCard from "../components/FindingCard";
import { useState } from "react";


export default function LiveScanPage() {
    const location = useLocation();
    const url = location.state?.url;
    const [currentPage, setCurrentPage] = useState(3);
    const totalPages = 10;
    const progress = (currentPage / totalPages) * 100; 
    const [functionalityFindings, setFunctionalityFindings] = useState([
        {
            id: 1,
            severity: "High",
            title: "Checkout request failed",
            businessImpact: "Customers may be unable to complete purchases.",
            affectedpage: "/checkout",
            technicalDetails: "POST /checkout returned HTTP 500"
        },
        {
            id: 2,
            severity: "Medium",
            title: "Broken image detected",
            businessImpact: "Customers may see missing content or an unprofessional page.",
            affectedpage: "/products",
            technicalDetails: "POST /products returned HTTP 500"
        }
    ]);
    const [securityFindings, setSecurityFindings] = useState([
        {
            id: 1,
            severity: "High",
            title: "Missing security header",
            businessImpact: "The website may have less protection against certain browser-based attacks.",
            affectedPage: "/",
            technicalDetails: "Content-Security-Policy header not detected"
        }
    ]);
    const [accessibilityFindings, setAccessibilityFindings] = useState([
        {
            id: 1,
            severity: "Medium",
            title: "Image missing alt text",
            businessImpact: "Visitors using screen readers may not understand important page content.",
            affectedPage: "/home",
            technicalDetails: "Image element missing alt attribute"
        }
    ]);

    return (
        <div>
            <h1>Live Scan</h1>
            <p>Scanning: {url}</p>
            <p>Scanning page {currentPage} out of {totalPages}.</p>

            <div style={{ width: "300px", height: "20px", backgroundColor: "#ddd" }}>
                <div 
                    style={{ 
                        width: `${progress}%`,
                        height: "100%",
                        backgroundColor: "black" 
                    }}
                ></div>
            </div>

            <button onClick={() => setCurrentPage(currentPage + 1)}>
                Next Page
            </button>

            <div>
                <h2>Security</h2>

                {securityFindings.map((finding) => (
                    <FindingCard key={finding.id} finding={finding} />
                ))}
            </div>

            <div>
                <h2>Functionality</h2>

                {functionalityFindings.map((finding) => (
                    <FindingCard key={finding.id} finding={finding} />
                ))}
            </div>

            <div>
                <h2>Accessibility</h2>

                {accessibilityFindings.map((finding) => (
                    <FindingCard key={finding.id} finding={finding} />
                ))}
            </div>

        </div>
    );
}