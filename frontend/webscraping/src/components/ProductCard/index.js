import { useNavigate } from "react-router-dom";

const ProductCard = ({product}) => {
    
    const navigate = useNavigate();
    const handleClick = () => {
        if(product.KeyboardId !== undefined){
        navigate(`/keyboard/${product.KeyboardId}`);
        }
        else if(product.HeadGearId !== undefined){
            navigate(`/headgear/${product.HeadGearId}`);
            }
    }
    if(product.Banana === 0){
        var cost = product.Ihavecpu
    }else{
        var cost = product.Banana
    }

    return (
        <>
        
        <div className="max-w-sm rounded overflow-hidden shadow-lg hover:cursor-pointer" onClick={handleClick}>
            <div>
            <div className=""><img
                className=" h-40 w-full object-contain pt-5"
                src={product.PictureLink}
                alt="Sunset in the mountains"
            />
            </div>
            <div className="px-6">
                <div className="text-xl mb-10">
                    {product.RegularName}
                </div>
                <p className="text-gray-700 text-xl font-bold">{cost+" บาท"}</p>
            </div>
            <div className="px-6 pt-4 pb-2">
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    {"#"+ product.Brand}
                </span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    #travel
                </span>
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    #winter
                </span>
            </div>
            </div>
            
           
            
        </div>
        
        </>
    );
};

export default ProductCard;
