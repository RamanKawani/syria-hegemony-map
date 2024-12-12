import React, { useEffect, useState } from 'react';
import L from 'leaflet';

const MapComponent = () => {
    const [regions, setRegions] = useState([]);

    useEffect(() => {
        fetch('/api/region/Idlib')
            .then(res => res.json())
            .then(data => setRegions(data));
    }, []);

    useEffect(() => {
        const map = L.map('map').setView([34.8021, 38.9968], 6); // Coordinates for Syria

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Add markers or regions dynamically based on data
        regions.forEach(region => {
            L.marker([region.lat, region.lng]).addTo(map)
                .bindPopup(`<b>${region.name}</b><br>${region.influenceLevel}`);
        });
    }, [regions]);

    return <div id="map" style={{ height: '500px' }}></div>;
};

export default MapComponent;
