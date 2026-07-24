import type { Metadata } from "next";
import {Roboto} from "next/font/google";
import "./globals.css";
import Header from "@/components/Header/header";


export const roboto = Roboto({
  weight: ["400", "500", "700"],
  subsets: ["latin"],
  variable: "--font-roboto",
});

export const metadata: Metadata = {
  title: "Mini Inbox",
  description: "Sistema de gerenciamento de tickets",
}

interface RootLayoutProps {
  children: React.ReactNode
}

export default function RootLayout({
  children,
}: Readonly<RootLayoutProps>) {
  return (
    <html
      lang="pt-br"
    >
      <body className={roboto.variable}>
        <Header />
        {children}
      </body>
    </html>
  );
}
