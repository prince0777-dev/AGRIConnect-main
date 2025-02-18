import { useState } from "react";

const ProductForm = () => {
    const [cropType, setCropType] = useState(0);
    const [region, setRegion] = useState(1);
    const [season, setSeason] = useState(0);
    const [quantity, setQuantity] = useState("");
    const [predictedPrice, setPredictedPrice] = useState(null);

    const getPrediction = async () => {
        const response = await fetch("https://your-api.com/predict-price/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ crop_type: cropType, region, season, quantity: parseFloat(quantity) })
        });
        const data = await response.json();
        setPredictedPrice(data.predicted_price);
    };

    return (
        <div>
            <h2>List a Product</h2>
            <label>Crop Type:</label>
            <select onChange={(e) => setCropType(parseInt(e.target.value))}>
                <option value="0">Wheat</option>
                <option value="1">Rice</option>
            </select>

            <label>Region:</label>
            <select onChange={(e) => setRegion(parseInt(e.target.value))}>
                <option value="1">North</option>
                <option value="2">South</option>
            </select>

            <label>Season:</label>
            <select onChange={(e) => setSeason(parseInt(e.target.value))}>
                <option value="0">Winter</option>
                <option value="1">Summer</option>
            </select>

            <label>Quantity (kg):</label>
            <input type="number" onChange={(e) => setQuantity(e.target.value)} />

            <button onClick={getPrediction}>Predict Price</button>

            {predictedPrice && <h3>Predicted Price: ₹{predictedPrice}</h3>}
        </div>
    );
};

export default ProductForm;
