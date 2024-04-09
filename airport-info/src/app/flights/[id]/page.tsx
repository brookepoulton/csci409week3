export default function FlightRoute({ params } : { params: { id: string} }) {
    return (
        <div>Hello from Flight # {params.id}</div>
    );
}