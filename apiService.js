const fetchRegionData = async (regionName) => {
    const response = await fetch(`/api/region/${regionName}`);
    const data = await response.json();
    return data;
};

export { fetchRegionData };
