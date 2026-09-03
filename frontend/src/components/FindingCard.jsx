export default function FindingCard({ finding }) {
    return (
        <div>
            <p>{finding.severity}</p>
            <h3>{finding.title}</h3>
            <p>{finding.businessImpact}</p>
            <p>Affected Page: {finding.affectedpage}</p>
            <p>Technical Details: {finding.technicalDetails}</p>
        </div>
    );
}