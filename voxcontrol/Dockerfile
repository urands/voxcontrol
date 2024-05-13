FROM node:20

WORKDIR /voxcontrol

COPY package*.json .

RUN npm ci

COPY . .

CMD ["npm run build"]