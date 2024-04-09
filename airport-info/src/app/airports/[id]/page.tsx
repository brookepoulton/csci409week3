export default function AirportInfo({ params } : { params: { id: string} }) {
    return (
        <div>Hello from Airport # {params.id}</div>
    );
}