import Layout from "@/components/layout";
// import { usePageAnalytics } from "@/hooks";
import { NextPage } from "next";
import React from "react";

const TermsPage: NextPage = () => {
  // usePageAnalytics();
  return (
    <Layout title="Terms and Conditions">
      <div className="flex justify-center items-center md:mt-5">
        <div className="lex max-w-md flex-col gap-2">
          <h3>Terms and Conditions</h3>
          <p>Terms of use</p>
        </div>
      </div>
    </Layout>
  );
};

export default TermsPage;
