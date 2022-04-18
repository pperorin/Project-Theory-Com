import { useNavigate } from "react-router-dom";

const ProductCard = () => {
    const navigate = useNavigate();
    const handleClick = () => {
        navigate("/stuffinfo/name");
    }
    
    return (
        <div className="max-w-sm rounded overflow-hidden shadow-lg hover:cursor-pointer" onClick={handleClick}>
            <img
                className="object-cover h-48 w-full"
                src="https://www.jib.co.th/img_master/product/original/2020100508552442984_1.png"
                alt="Sunset in the mountains"
            />
            <div className="px-6">
                <div className="text-xl mb-10">
                    KEYBOARD (คีย์บอร์ด) HyperX ALLOY ORIGINS (HyperX BLUE SWITCH) (RGB LED) (EN/TH)
                </div>
                <p className="text-gray-700 text-xl font-bold">ราคา 3,290 บาท</p>
            </div>
            <div className="px-6 pt-4 pb-2">
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    #photography
                </span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    #travel
                </span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    #winter
                </span>
            </div>
        </div>
    );
};

export default ProductCard;
