import Layout from "@/components/layout";
import { NextPage } from "next";
import React from "react";
import { Stickers } from "@/modules/stocks/Stickers";
import dynamic from "next/dynamic";
// import { usePageAnalytics } from "@/hooks";

const Menus = dynamic(() => import("@/modules/stocks/Menus"), {
  ssr: false,
});

const StickersTablePage: NextPage = () => {
  // usePageAnalytics();
  return (
    <Layout title='Stickers'>
      <div className="float-left">
        <Menus />
      </div>
      <div className="flex justify-center items-center md:mt-5">
        <div className="flex max-w-md flex-col gap-2">
          <h5 className="mb-2 text-3xl font-bold text-gray-900 dark:text-white">
            Stickers
          </h5>
        </div>
      </div>
      <Stickers />
    </Layout>
  );
};

export default StickersTablePage;
