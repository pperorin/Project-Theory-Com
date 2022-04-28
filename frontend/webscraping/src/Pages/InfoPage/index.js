import { useState } from 'react';
import { PageLayout } from '../../components';
import { useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const Stuffinfo = () => {
    const { id } = useParams();
    const [loading, setLoading] = useState(true);
    const [info, setInfo] = useState();
    var price;
    var shop;

    useEffect(() => {
        const getdata = async () => {
            try {
                setLoading(true);
                const data = await axios.get(
                    'https://theorybackend.herokuapp.com/' + window.location.pathname.split('/')[1] + '/' + id
                );
                setInfo(data.data);

                // setProductcard(keyboard=>[...keyboard,data2.data])
                // setProductcard2(data2.data);
            } catch (err) {
                // toast.error(err.response.data.messsage);
            }
            setLoading(false);
        };

        getdata();
    }, [id]);
    if (!loading) {
        if (parseInt(info.Banana) > parseInt(info.Ihavecpu) && parseInt(info.Ihavecpu) !== 0) {
            price = info.Ihavecpu + ' - ' + info.Banana;
            shop = '2';
        } else if (parseInt(info.Ihavecpu) > parseInt(info.Banana) && parseInt(info.Banana) !== 0) {
            price = info.Banana + ' - ' + info.Ihavecpu;
            shop = '2';
        } else if (parseInt(info.Ihavecpu) > parseInt(info.Banana) && parseInt(info.Banana) === 0) {
            price = info.Ihavecpu;
            shop = '1';
        } else {
            price = info.Banana;
            shop = '1';
        }
    }

    return (
        <>
            <PageLayout>
                {loading ? (
                    <p>loading...</p>
                ) : (
                    <div className="flex flex-col w-full h-full justify-center">
                        <div className="grid grid-cols-5 grid-rows-2 gap-12 ">
                            <div className="flex flex-col h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-3 ">
                                <img className="bg-white h-96 w-96  object-cover " src={info.PictureLink} alt=""></img>
                                <div className="text-2xl">ร้านค้าที่จำหน่าย</div>
                            </div>
                            <div className="flex flex-col h-full w-full m-auto rounded-xl row-span-2 col-span-2 gap-2 ">
                                <div className="pt-20 text-ellipsis max-w-sm font-bold">{info.Name}</div>
                                <div className="pt-10 ">{price} บาท</div>

                                <div className=" ">มีทั้งหมด {shop} ร้านค้า</div>
                            </div>
                        </div>
                        {info.Banana !== '0' && (
                            <div className="flex flex-col   w-full h-full justify-between  ">
                                <div className="grid grid-cols-2 grid-rows-1 gap-12 ">
                                    <div className=" flex flex-col h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-1 pr-20 ">
                                        <div>
                                            <img
                                                className="bg-white h-40 w-40  object-contain "
                                                src="https://media.discordapp.net/attachments/802277621772714004/964625721106526208/unknown.png"
                                                alt=""
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div className="grid grid-cols-6 grid-rows-1 gap-12 ">
                                    <div className="flex flex-row h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-5 space-x-20 ">
                                        <div className="">{info.Name}</div>
                                        <div className="items-end">{info.Banana} บาท</div>
                                    </div>
                                </div>
                            </div>
                        )}
                        {info.Ihavecpu !== '0' && (
                            <div className="flex flex-col   w-full h-full justify-between ">
                                <div className="grid grid-cols-2 grid-rows-1 gap-12 ">
                                    <div className=" flex flex-col h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-1 pr-20 ">
                                        <div>
                                            <img
                                                className="bg-white h-40 w-40  object-contain "
                                                src="https://cf.shopee.co.th/file/0aa5de07c908febaf2a78af8a0587799"
                                                alt=""
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div className="grid grid-cols-6 grid-rows-1 gap-12 ">
                                    <div className="flex flex-row h-full w-full m-auto justify-center items-center rounded-xl row-span-2 col-span-5 space-x-20 ">
                                        <div className="">{info.Name}</div>
                                        <div className="items-end">{info.Ihavecpu} บาท</div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                )}
            </PageLayout>
        </>
    );
};
export default Stuffinfo;
