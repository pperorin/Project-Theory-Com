import NavigationBar from "./NavigationBar";
function stuffinfo(){

    return(
        <>
        <NavigationBar/>
        <div className="flex flex-col w-full h-full justify-center">
            <div  className="grid grid-cols-5 grid-rows-2 gap-12 ">
                
                <div className="flex flex-col h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-3 ">
                        <img
                        className="bg-white h-96 w-96  object-contain "
                        src="https://media.discordapp.net/attachments/802277621772714004/964617308238655558/unknown.png?width=1031&height=488"
                       
                        ></img>
                        <div className="text-2xl">ร้านค้าที่จำหน่าย</div>
                </div>
                <div className="flex flex-col h-full w-full m-auto rounded-xl row-span-2 col-span-2 gap-2 ">
                    <div className="pt-20 text-ellipsis max-w-sm">Signo Gaming Keyboard INDIGO MINI RGB Mechanical คีย์บอร์ดเกม รุ่น KB-718</div>
                    <div className="pt-10 " >ราคา799-2070</div>  
                    <div className=" " >มีทั้งหมด 5ร้านค้า</div> 
                </div>
                
            </div>
            <div className="flex flex-col   w-full h-full justify-center  ">
                <div  className="grid grid-cols-2 grid-rows-1 gap-12 ">
                    <div className=" flex flex-col h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-1 pr-20 ">
                        <div><img  className="bg-white h-40 w-40  object-contain "
                        src="https://media.discordapp.net/attachments/802277621772714004/964625721106526208/unknown.png" alt="" /></div>
                        
                        
                    </div>
                   
                    
                </div>    
                <div  className="grid grid-cols-6 grid-rows-1 gap-12 ">
                    <div className="flex flex-row h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-5 space-x-20 ">
                                <div className="">Signo Gaming Keyboard INDIGO KB-718 MINI RGB Mechanical Blue Switches (Optical SW)</div>
                                <div className="items-end">990</div>
                            </div>
                </div>
            </div>
            

            
            
        </div>
        </>
    );
}
export default stuffinfo;